const express = require("express");
const session = require("express-session");

const buildManifest = require("./manifest_build").buildManifest;
const summarizeWindow = require("./summarize_window").summarizeWindow;
const fetchCheckpoint = require("./fetch_checkpoint").fetchCheckpoint;
const resolveShipment = require("./resolve_shipment").resolveShipment;
const archiveConfig = require("./archive_config").archiveConfig;
const buildCheckpoint = require("./build_checkpoint").buildCheckpoint;
const buildBatch = require("./build_batch").buildBatch;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/buildManifest", buildManifest);
app.post("/summarizeWindow", summarizeWindow);
app.post("/fetchCheckpoint", fetchCheckpoint);
app.post("/resolveShipment", resolveShipment);
app.post("/archiveConfig", archiveConfig);
app.post("/buildCheckpoint", buildCheckpoint);
app.post("/buildBatch", buildBatch);

app.listen(3000, "0.0.0.0");
