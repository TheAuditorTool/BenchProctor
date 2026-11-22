const express = require("express");
const session = require("express-session");

const storeArchive = require("./archive_store").storeArchive;
const summarizeConfig = require("./summarize_config").summarizeConfig;
const compactIndex = require("./compact_index").compactIndex;
const archiveSchedule = require("./archive_schedule").archiveSchedule;
const formatRedaction = require("./format_redaction").formatRedaction;
const archiveBundle = require("./archive_bundle").archiveBundle;
const verifyPolicy = require("./verify_policy").verifyPolicy;
const reconcilePolicy = require("./reconcile_policy").reconcilePolicy;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/storeArchive", storeArchive);
app.post("/summarizeConfig/:id", summarizeConfig);
app.post("/compactIndex", compactIndex);
app.post("/archiveSchedule", archiveSchedule);
app.post("/formatRedaction", formatRedaction);
app.post("/archiveBundle", archiveBundle);
app.post("/verifyPolicy", verifyPolicy);
app.post("/reconcilePolicy", reconcilePolicy);

app.listen(3000, "0.0.0.0");
