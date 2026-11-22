const express = require("express");
const session = require("express-session");

const verifySignature = require("./signature_verify").verifySignature;
const archiveWebhook = require("./archive_webhook").archiveWebhook;
const publishWindow = require("./publish_window").publishWindow;
const auditPartner = require("./audit_partner").auditPartner;
const auditBatch = require("./audit_batch").auditBatch;
const validateCheckpoint = require("./validate_checkpoint").validateCheckpoint;
const summarizeCheckpoint = require("./summarize_checkpoint").summarizeCheckpoint;
const reconcileRecord = require("./reconcile_record").reconcileRecord;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/verifySignature", verifySignature);
app.post("/archiveWebhook", archiveWebhook);
app.post("/publishWindow", publishWindow);
app.post("/auditPartner", auditPartner);
app.post("/auditBatch", auditBatch);
app.post("/validateCheckpoint", validateCheckpoint);
app.post("/summarizeCheckpoint", summarizeCheckpoint);
app.post("/reconcileRecord", reconcileRecord);

app.listen(3000, "0.0.0.0");
