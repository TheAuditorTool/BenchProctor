const express = require("express");
const session = require("express-session");

const storeArchive = require("./archive_store").storeArchive;
const summarizeManifest = require("./summarize_manifest").summarizeManifest;
const formatRedaction = require("./format_redaction").formatRedaction;
const loadBundle = require("./load_bundle").loadBundle;
const resolveBundle = require("./resolve_bundle").resolveBundle;
const rotateCheckpoint = require("./rotate_checkpoint").rotateCheckpoint;
const archiveBundle = require("./archive_bundle").archiveBundle;
const mergeLedger = require("./merge_ledger").mergeLedger;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/storeArchive", storeArchive);
app.post("/summarizeManifest", summarizeManifest);
app.post("/formatRedaction", formatRedaction);
app.post("/loadBundle", loadBundle);
app.post("/resolveBundle", resolveBundle);
app.post("/rotateCheckpoint", rotateCheckpoint);
app.post("/archiveBundle", archiveBundle);
app.post("/mergeLedger", mergeLedger);

app.listen(3000, "0.0.0.0");
