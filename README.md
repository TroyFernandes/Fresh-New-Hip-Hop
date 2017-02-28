# Fresh-New-Hip-Hop
Amazon Alexa Skill that Gets All [FRESH] Songs From r/HipHopHeads

This skill allows you to ask Amazon Alexa to check whats [FRESH] on r/HipHopHeads. You can also ask for the link to be sent to your Amazon Alexa companion app. Right now Amazon dosen't allow hyperlinks to be sent to the companion app (not sure why) so for now its in plain text. But when they allow that ... 👌

You can specify your favourite artists and Alexa will check if there's any new songs by them.

# Setup
   1. Sign into the [Amazon Developer Portal](https://developer.amazon.com/) and click the Alexa Tab
   2. Click "Add a New Skill"
   3. Enter the info for skill information, and click next
      ![](https://github.com/TroyFernandes/Fresh-New-Hip-Hop/blob/master/Setup%20Images/Skill%20info.JPG)
   5. Here is the code you paste in [Intent Schema](https://github.com/TroyFernandes/Fresh-New-Hip-Hop/blob/master/speechAssets/IntentSchema.json)
         
   6. For custom slot types, the "Type" = ARTISTS . Enter your favourite artists in the values. Each line should be a different                  artist
   7. For sample utterances, paste this [in](https://github.com/TroyFernandes/Fresh-New-Hip-Hop/blob/master/speechAssets/SampleUtterances.txt) click next when done
      ![](https://github.com/TroyFernandes/Fresh-New-Hip-Hop/blob/master/Setup%20Images/Interaction%20Model.png)
   8. For the configuration tab, select HTTPS then North America or Europe depending on location. Paste in your ngrok HTTPS link followed by /fresh_new_hip_hop ![](https://github.com/TroyFernandes/Fresh-New-Hip-Hop/blob/master/Setup%20Images/ngrok.JPG) It should look like this ![](https://github.com/TroyFernandes/Fresh-New-Hip-Hop/blob/master/Setup%20Images/Configuration.JPG)
   9. For the SSL Certification tab, choose "My development endpoint is a sub domain of a domain that has a wildcard certificate ... " Click next
   10. Done!

# Sample Use

Here's a quick example of the interaction. U = user, A = Amazon Alexa.
   - U: Echo, start fresh new hip hop
   - A: Hello! you wanna know whats fresh on r/hiphopheads?
   - U: Only from my favourite artists
   - A: The newest tracks from your favourite artists today are Madeintyo - Thank you, Mr. Tokyo
   - U: send me the link for Madeintyo
   - A: Sending the link for [FRESH] Madeintyo - Thank you, Mr. Tokyo
   
