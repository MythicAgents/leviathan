# Leviathan

leviathan is a Chrome Extension payload that's designed to live in the browser and be hosted on your own infrastructure (not within Google Chrome's store). This leviathan instance supports Mythic 2.2 and will updated as necessary. It does not support Mythic 2.1 and lower.

The agent has `mythic_payloadtype_container==0.0.42` PyPi package installed and reports to Mythic as version "6".

## How to install an agent in this format within Mythic

When it's time for you to test out your install or for another user to install your agent, it's pretty simple. Within Mythic is a `install_agent_from_github.sh` script (https://github.com/its-a-feature/Mythic/blob/master/install_agent_from_github.sh). You can run this in one of two ways:

* `sudo ./install_agent_from_github.sh https://github.com/user/repo` to install the main branch
* `sudo ./install_agent_from_github.sh https://github.com/user/repo branchname` to install a specific branch of that repo

Now, you might be wondering _when_ should you or a user do this to properly add your agent to their Mythic instance. There's no wrong answer here, just depends on your preference. The three options are:

* Mythic is already up and going, then you can run the install script and just direct that agent's containers to start (i.e. `sudo ./start_payload_types.sh agentName` and if that agent has its own special C2 containers, you'll need to start them too via `sudo ./start_c2_profiles.sh c2profileName`).
* Mythic is already up and going, but you want to minimize your steps, you can just install the agent and run `sudo ./start_mythic.sh`. That script will first _stop_ all of your containers, then start everything back up again. This will also bring in the new agent you just installed.
* Mythic isn't running, you can install the script and just run `sudo ./start_mythic.sh`. 

