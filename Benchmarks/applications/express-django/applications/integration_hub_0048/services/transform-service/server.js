const express = require("express");
const session = require("express-session");

const transformPayload = require("./payload_transform").transformPayload;
const annotateSnapshot = require("./annotate_snapshot").annotateSnapshot;
const normalizeLedger = require("./normalize_ledger").normalizeLedger;
const loadMapping = require("./load_mapping").loadMapping;
const rotateCheckpoint = require("./rotate_checkpoint").rotateCheckpoint;
const publishMapping = require("./publish_mapping").publishMapping;
const buildWebhook = require("./build_webhook").buildWebhook;
const compactCheckpoint = require("./compact_checkpoint").compactCheckpoint;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/transformPayload", transformPayload);
app.post("/annotateSnapshot", annotateSnapshot);
app.post("/normalizeLedger/:id", normalizeLedger);
app.post("/loadMapping", loadMapping);
app.post("/rotateCheckpoint", rotateCheckpoint);
app.post("/publishMapping", publishMapping);
app.post("/buildWebhook", buildWebhook);
app.post("/compactCheckpoint", compactCheckpoint);

app.listen(3000, "0.0.0.0");
