+++
title = "motion canvas js plan and code snippets.md"
date = "2024-08-10"
+++
Goal: To generate video chunks without the need to record. Fast, EASY, and simple.
## Features
- 2 size layouts
	- Support any media to show left and right.
		- Notes below show a good example!
- type writer
	- letter by letter base on sentence
- markdown notes
	- generate video showing notes by appending them

## Goodies
- Parametrize Scenes  - Jocab Discord Server guide
	- This is honestly as far as I need. No need to do the command line idea cause that seems like trouble.

make your own scene ...
```
import {waitFor, waitUntil} from '@motion-canvas/core'; import {makeParametrizedScene} from '../utils'; // The second argument after `view` are the params passed to us from // the outsize. Here we use a simple string as a color but it could // be anything: export default makeParametrizedScene(function* (view, color: string) { view.fill(color); yield* waitFor(1); yield* waitUntil('event'); });
```

How it is used...
```
import {makeProject} from '@motion-canvas/core'; import example from './scenes/example?scene'; import {parametrize} from './utils'; export default makeProject({ scenes: [ parametrize(example, 'red'), parametrize(example, 'green'), parametrize(example, 'blue'), ], });


OR


const colors = ['red', 'green', 'blue']; export default makeProject({ scenes: colors.map(color => parametrize(example, color)), });

```

Showing Markdown/List of Objects
-  example of someone else doing it
	- https://github.com/CactusPuppy/motion-canvas-projects/blob/main/src/scenes/demon-lord/credits/credits.tsx
	- NOTE
	- https://github.com/ksassnowski/motion-canvas-camera

```
  // yield* creditsContainer().bottom([0, -useScene().getSize().height / 2], useDuration("creditsScroll"), linear);
  const targetDuration = usePlayback().secondsToFrames(useDuration("creditsScroll"));
  const distance = Math.ceil(-useScene().getSize().height / 2 - creditsContainer().size().y / 2) - creditsY();
  const waitDuration = usePlayback().framesToSeconds(Math.abs(targetDuration / distance));
```
automatic slowing to match

```
This code is how they converted md to motionjs layouts
super cool.

function convertCreditToJSX(credit: string) {
  const logger = useLogger();
  credit = credit.trim();
  const creditDisplay = credit.replace(/\\n/g, "\n");
  const containsNewlines = creditDisplay.includes("\n");

  // Separator line
  if (credit.match(/^-{3,}$/)) {
    // logger.info("Separator line");
    return (<Rect width="80%" height={4} fill="white" marginTop={16} marginBottom={16}/>);
  }

  // TITLE
  if (credit.startsWith("# ")) {
    return (<Txt fill="white" fontFamily={"Config Monospace"} fontWeight={200} fontSize={60} textWrap={containsNewlines ? "pre" : true} textAlign={"center"}>
      {creditDisplay.slice(2)}
    </Txt>);
  }
  // HEADING
  if (credit.startsWith("## ")) {
    return (<Txt fill="white" fontFamily={"Config"} fontWeight={600} fontSize={36} marginBottom={-16} textWrap={containsNewlines ? "pre" : true} textAlign={"center"} >
      {creditDisplay.slice(3)}
    </Txt>);
  }
  // Main credit
  if (credit.startsWith("* ")) {
    return (<Txt fill="white" fontFamily={"Industry"} fontWeight={600} fontSize={26} textWrap={containsNewlines ? "pre" : true} textAlign={"center"}>
      {creditDisplay.slice(2)}
    </Txt>);
  }

  // GRID
  if (credit.match(/^\\ (.*?) \| (.*)$/)) {
    const match = credit.match(/^\\ (.*?) \| (.*)$/);

    const creditGrid = createRef<Layout>();
    const creditTitleAnchor = createRef<Layout>();
    const creditTitle = createRef<Layout>();
    const creditContentAnchor = createRef<Layout>();
    const creditContent = createRef<Layout>();
    const height = createSignal(0);

    const result = (<Layout layout direction="row" width="100%" height={() => height()} ref={creditGrid} gap={16}>
      <Layout ref={creditTitleAnchor} grow={1} />
      <Layout layout={false} ref={creditTitle} height={() => height()}>
        <Txt fill="white" topRight={() => [creditTitle().size().x / 2, -creditTitle().size().y / 2]} fontFamily={"Industry"} fontWeight={600} fontSize={26} textAlign={"right"} textWrap={"pre"}>{match[1].replace("\\n", "\n")}</Txt>
      </Layout>
      <Layout ref={creditContentAnchor} grow={1} />
      <Layout layout={false} ref={creditContent} height={() => height()}>
        <Node y={1}>
          <Txt fill="white" topLeft={() => [-creditContent().size().x / 2, -creditContent().size().y / 2]} fontSize={26} textAlign={"left"} fontFamily={"Barlow"} textWrap={"pre"} fontWeight={300}>{match[2].split(", ").join("\n")}</Txt>
        </Node>
      </Layout>
    </Layout>);

    height(() => Math.max(creditTitle().findFirst<Txt>(node => node instanceof Txt).size().y, creditContent().findFirst<Txt>(node => node instanceof Txt).size().y));

    creditTitle().bottomRight(() => creditTitleAnchor().bottomRight());
    creditContent().bottomLeft(() => creditContentAnchor().bottomLeft());

    return result;
  }

  // GRID 3 COLUMN
  if (credit.startsWith("||| ")) {
    const allNames = creditDisplay.slice(4).split(", ");
    const columnLength = Math.ceil(allNames.length / 3);
    const column1 = allNames.slice(0, columnLength);
    const column2 = allNames.slice(columnLength, columnLength * 2);
    const column3 = allNames.slice(columnLength * 2);

    return (<Layout layout direction="row" marginTop={-24} width={850}>
      <Layout direction="column" gap={4} grow={1}>
        {column1.map((name) => <Txt fill="white" fontFamily={"Barlow"} fontWeight={300} fontSize={20} text={name} textAlign={"left"} />)}
      </Layout>
      <Layout direction="column" gap={4} grow={1}>
        {column2.map((name) => <Txt fill="white" fontFamily={"Barlow"} fontWeight={300} fontSize={20} text={name} textAlign={"left"} />)}
      </Layout>
      <Layout direction="column" gap={4} grow={1}>
        {column3.map((name) => <Txt fill="white" fontFamily={"Barlow"} fontWeight={300} fontSize={20} text={name} textAlign={"left"} />)}
      </Layout>
    </Layout>);
  }

  // Normal
  if (credit.trim() != "") {
    return (<Txt fill="white" fontFamily={"Barlow"} fontWeight={300} fontSize={26} marginTop={-32} textWrap={containsNewlines ? "pre" : true} textAlign={"center"}>
      {creditDisplay}
    </Txt>);
  }

  return (<></>);
}
```