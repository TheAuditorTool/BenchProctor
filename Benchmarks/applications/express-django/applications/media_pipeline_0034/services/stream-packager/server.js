const express = require("express");
const session = require("express-session");

const buildManifest = require("./stream_manifest").buildManifest;
const enrichSchedule = require("./enrich_schedule").enrichSchedule;
const loadCaption = require("./load_caption").loadCaption;
const validateBundle = require("./validate_bundle").validateBundle;
const prunePolicy = require("./prune_policy").prunePolicy;
const archiveRecord = require("./archive_record").archiveRecord;
const mergeReceipt = require("./merge_receipt").mergeReceipt;
const fetchConfig = require("./fetch_config").fetchConfig;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/buildManifest/:id", buildManifest);
app.post("/enrichSchedule", enrichSchedule);
app.post("/loadCaption", loadCaption);
app.post("/validateBundle", validateBundle);
app.post("/prunePolicy", prunePolicy);
app.post("/archiveRecord", archiveRecord);
app.post("/mergeReceipt", mergeReceipt);
app.post("/fetchConfig", fetchConfig);

app.listen(3000, "0.0.0.0");
