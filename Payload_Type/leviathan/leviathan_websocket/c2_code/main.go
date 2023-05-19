package main

import (
	"encoding/json"
	"github.com/MythicC2Profiles/websocket/servers"
	"io"
	"log"
	"os"
)

func main() {
	c2config := servers.C2Config{}
	if cf, err := os.Open("config.json"); err != nil {
		log.Println("Error opening config file ", err.Error())
		os.Exit(-1)
	} else if config, err := io.ReadAll(cf); err != nil {
		log.Println("Error in reading config file ", err.Error())
		os.Exit(-1)
	} else if err = json.Unmarshal(config, &c2config); err != nil {
		log.Println("Error in unmarshal call for config ", err.Error())
		os.Exit(-1)
	}
	// start the server instance with the config
	c2server := servers.NewInstance().(servers.Server)

	c2server.Run(c2config)

}
