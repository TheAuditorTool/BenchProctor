const express = require("express");
const session = require("express-session");

const transformPayload = require("./payload_transform").transformPayload;
const reconcileLedger = require("./reconcile_ledger").reconcileLedger;
const compactConnector = require("./compact_connector").compactConnector;
const resolveCheckpoint = require("./resolve_checkpoint").resolveCheckpoint;
const archivePolicy = require("./archive_policy").archivePolicy;
const resolveDigest = require("./resolve_digest").resolveDigest;
const formatRecord = require("./format_record").formatRecord;
const exportBatch = require("./export_batch").exportBatch;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/transformPayload", transformPayload);
app.post("/reconcileLedger", reconcileLedger);
app.post("/compactConnector", compactConnector);
app.post("/resolveCheckpoint", resolveCheckpoint);
app.post("/archivePolicy", archivePolicy);
app.post("/resolveDigest", resolveDigest);
app.post("/formatRecord", formatRecord);
app.post("/exportBatch", exportBatch);

app.listen(3000, "0.0.0.0");
