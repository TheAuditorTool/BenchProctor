const express = require("express");
const session = require("express-session");

const registerMandate = require("./mandate_register").registerMandate;
const enrichRoster = require("./enrich_roster").enrichRoster;
const verifyBatch = require("./verify_batch").verifyBatch;
const verifyRoster = require("./verify_roster").verifyRoster;
const mergeReport = require("./merge_report").mergeReport;
const compactConfig = require("./compact_config").compactConfig;
const mergeThreshold = require("./merge_threshold").mergeThreshold;
const archiveSnapshot = require("./archive_snapshot").archiveSnapshot;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/registerMandate", registerMandate);
app.post("/enrichRoster/:id", enrichRoster);
app.post("/verifyBatch", verifyBatch);
app.post("/verifyRoster", verifyRoster);
app.post("/mergeReport", mergeReport);
app.post("/compactConfig", compactConfig);
app.post("/mergeThreshold", mergeThreshold);
app.post("/archiveSnapshot", archiveSnapshot);

app.listen(3000, "0.0.0.0");
