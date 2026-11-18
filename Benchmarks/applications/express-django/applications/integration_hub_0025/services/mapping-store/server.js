const express = require("express");
const session = require("express-session");

const mapField = require("./field_mapping").mapField;
const archiveRecord = require("./archive_record").archiveRecord;
const mergePolicy = require("./merge_policy").mergePolicy;
const verifyConfig = require("./verify_config").verifyConfig;
const publishReport = require("./publish_report").publishReport;
const enrichCheckpoint = require("./enrich_checkpoint").enrichCheckpoint;
const archiveReceipt = require("./archive_receipt").archiveReceipt;
const rotateReceipt = require("./rotate_receipt").rotateReceipt;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/mapField", route(mapField));
app.post("/archiveRecord", route(archiveRecord));
app.post("/mergePolicy", route(mergePolicy));
app.post("/verifyConfig", route(verifyConfig));
app.post("/publishReport", route(publishReport));
app.post("/enrichCheckpoint", route(enrichCheckpoint));
app.post("/archiveReceipt", route(archiveReceipt));
app.post("/rotateReceipt", route(rotateReceipt));

app.listen(3000, "0.0.0.0");
