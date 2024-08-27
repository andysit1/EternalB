+++
title = "overview.md"
date = "2024-08-26"
+++

---
**Key Timestamps**
- Basics
	- 0:07:00 Basic Controls
- Settings
	- 0:04:20 Title editor / Triggers
- Audio
	- 0:16:43 Start of Audio Routing
- Route/Port
	- 0:28:18 Route and Audio Port
	- 0:32:00 srt stream
- NDI
	- great for single stream setup
	- 0:11:30 NDI Plugin is required to go from vmix -> obs stream 

**Understanding vMix Audio Monitoring and Setup**

1. **Audio Monitoring:**
   - To monitor audio, you can enable the monitoring feature. This lets you hear feedback through your headphones. Be cautious, as this means you'll hear everything, including the music playing on the stream, which can result in hearing the audio twice. Most people keep the monitoring volume low or at zero to avoid confusion.
   
   - "It's really easy to monitor audio. You can turn on monitoring, which means you'll hear feedback through your own headphones. Be careful with this setting as it can sometimes result in hearing your stream's audio twice, which is great if you want to avoid deafening the stream. Usually, I keep it set to zero."

3. **Input and Output Management:**
   - "You can adjust the volume using the dials for the main buses. These are really straightforward. We have actual inputs and outputs, with each having multiple options for control."

5. **Setting Up Audio:**
   - Inputs are the sources of audio, while outputs are what you send out. In vMix, you have three main outputs. For example, you might send music through the master output, so the casters don't hear it. Microphone audio is routed through a specific bus, and game audio from observers can be routed to both the master and another bus.
              
   - You have several audio buses (main channels) to control the volume levels of different audio sources. The main buses allow you to adjust the volume for various audio inputs, such as microphones and music. 

   - "For music, we're sending it only through the master bus so the casters don’t hear it. The microphone is routed through Bus A, and game audio from each observer is routed through both the master and Bus A. All caster calls are sent only through the master bus."

7. **Layer Management:**
   - In vMix, you can manage different layers, like overlays and video feeds. Each layer can be toggled on or off, but remember that audio will still be active even if the visual layer is turned off. This is important for keeping audio from different sources properly managed. 
   
   - "Layers allow you to organize your inputs and visuals. You can toggle layers on or off, but it's important to ensure that audio still comes through even if a layer is turned off. For example, if you switch layers, ensure that all necessary audio channels remain active."

8. **Adjusting and Toggling Inputs:**

   - "When switching to different layers, you may need to disable or adjust inputs accordingly. This ensures only the desired audio is active in each layer. The 'automatic mixing' option for inputs can help manage this."

9. **Handling SRT Streams:**
   - When adding an SRT (Secure Reliable Transport) stream, you need to set up the correct latency to handle delays. The latency setting should be at least **500 milliseconds** to prevent artifacts. Hardware decoding can help with performance.

   - "To add an SRT (Secure Reliable Transport) stream, go to the stream settings and select 'Listen.' Choose a port number (avoid low numbers like 80 for security reasons). Set the latency to at least 500 ms to avoid artifacts. Remember, you cannot adjust latency after setup, so choose carefully."

10. **Port Forwarding:**
   - To stream directly to your PC, you might need to configure port forwarding on your router. This involves allowing specific ports to communicate with your PC while maintaining security. Avoid using low-numbered ports as they can be less secure.
   
   - "Port forwarding is crucial for ensuring that traffic from the internet reaches your vMix setup. Configure your router to forward specific ports to your PC. This helps in allowing direct communication for streaming, though be cautious of security risks associated with low-numbered ports."

12. **Setting Up Profiles and Test Runs:**
   - "You can create new profiles for different streaming setups. For testing, use a profile to simulate your stream and check settings. If you need assistance with this, a test run can be helpful."

13. **Using Overlays and Picture-in-Picture:**
   - "To set up overlays or picture-in-picture, go to the overlay settings and adjust the positioning, zoom, and cropping. This allows you to manage how different visual elements are displayed during the stream."

14. **Shortcuts and Customization:**
	- Use triggers and shortcuts to quickly control various aspects of your production. For instance, you can assign shortcuts for turning microphones on and off or switching between different video feeds.

    - "Utilize keyboard shortcuts for quick access to frequently used functions. For example, setting up shortcuts to control microphone on/off or switching between different views can streamline your workflow."
---

