const express = require("express");
const session = require("express-session");

const validateAddress = require("./address_validate").validateAddress;
const summarizeShipment = require("./summarize_shipment").summarizeShipment;
const enrichIndex = require("./enrich_index").enrichIndex;
const validateDigest = require("./validate_digest").validateDigest;
const exportSummary = require("./export_summary").exportSummary;
const fetchDigest = require("./fetch_digest").fetchDigest;
const exportReceipt = require("./export_receipt").exportReceipt;
const pruneCheckpoint = require("./prune_checkpoint").pruneCheckpoint;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/validateAddress", validateAddress);
app.post("/summarizeShipment", summarizeShipment);
app.post("/enrichIndex", enrichIndex);
app.post("/validateDigest", validateDigest);
app.post("/exportSummary", exportSummary);
app.post("/fetchDigest", fetchDigest);
app.post("/exportReceipt", exportReceipt);
app.post("/pruneCheckpoint", pruneCheckpoint);

app.listen(3000, "0.0.0.0");
