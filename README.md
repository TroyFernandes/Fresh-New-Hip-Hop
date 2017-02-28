# Fresh-New-Hip-Hop
Amazon Alexa Skill that Gets All [FRESH] Songs From r/HipHopHeads

This skill allows you to ask Amazon Alexa to check whats [FRESH] on r/HipHopHeads. You can also ask for the link to be sent to your Amazon Alexa companion app. Right now Amazon dosen't allow hyperlinks to be sent to the companion app (not sure why) so for now its in plain text. But when they allow that ... 👌

You can specify your favourite artists and Alexa will check if there's any new songs by them.

# Setup
   1. Sign into the [Amazon Developer Portal](https://developer.amazon.com/) and click the Alexa Tab
   2. Click "Add a New Skill"
   3. Enter the info for skill information. 
      ![](https://github.com/TroyFernandes/Fresh-New-Hip-Hop/blob/master/Setup%20Images/Skill%20info.JPG)
   4. Enter the info for the interaction model. [link](https://github.com/TroyFernandes/Fresh-New-Hip-Hop/tree/master/speechAssets)
         * [Intent Schema](https://github.com/TroyFernandes/Fresh-New-Hip-Hop/blob/master/speechAssets/IntentSchema.json)
         
         * For custom slot types, the "Type" = ARTISTS . Enter your favourite artists in the values. Each line should be a different                  artist
         
      ![](https://github.com/TroyFernandes/Fresh-New-Hip-Hop/blob/master/Setup%20Images/Interaction%20Model.png)
