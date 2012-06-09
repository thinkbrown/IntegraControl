
<cfsavecontent variable="cacheManifest">

CACHE MANIFEST

# Core files.

./index.html
./zone2.html
 
# iPhone App files (for full-screen app mode).
./img/logo.png
./img/startup.png
 
# Images that get viewed.
./img/on.png
./img/off.png
./img/volup.png
./img/voldown.png
./img/mute.png
 
</cfsavecontent>
 
<cfcontent
	type="text/cache-manifest"
	variable="#toBinary( toBase64( trim( cacheManifest ) ) )#"
	/>
