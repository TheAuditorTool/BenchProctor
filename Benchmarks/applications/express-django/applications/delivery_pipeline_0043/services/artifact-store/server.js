const express = require("express");
const session = require("express-session");

const publishArtifact = require("./artifact_publish").publishArtifact;
const verifyHeader = require("./verify_header").verifyHeader;
const loadSummary = require("./load_summary").loadSummary;
const pruneReport = require("./prune_report").pruneReport;
const archiveSummary = require("./archive_summary").archiveSummary;
const annotateWindow = require("./annotate_window").annotateWindow;
const compactPolicy = require("./compact_policy").compactPolicy;
const summarizeReport = require("./summarize_report").summarizeReport;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/publishArtifact", publishArtifact);
app.post("/verifyHeader", verifyHeader);
app.post("/loadSummary", loadSummary);
app.post("/pruneReport", pruneReport);
app.post("/archiveSummary", archiveSummary);
app.post("/annotateWindow", annotateWindow);
app.post("/compactPolicy", compactPolicy);
app.post("/summarizeReport", summarizeReport);

app.listen(3000, "0.0.0.0");
