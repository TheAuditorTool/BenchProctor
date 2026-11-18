const express = require("express");
const session = require("express-session");

const storeArchive = require("./archive_store").storeArchive;
const annotateRedaction = require("./annotate_redaction").annotateRedaction;
const annotateReceipt = require("./annotate_receipt").annotateReceipt;
const mergeConversion = require("./merge_conversion").mergeConversion;
const publishManifest = require("./publish_manifest").publishManifest;
const verifyPolicy = require("./verify_policy").verifyPolicy;
const verifyConversion = require("./verify_conversion").verifyConversion;
const auditBatch = require("./audit_batch").auditBatch;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/storeArchive", route(storeArchive));
app.post("/annotateRedaction", route(annotateRedaction));
app.post("/annotateReceipt", route(annotateReceipt));
app.post("/mergeConversion", route(mergeConversion));
app.post("/publishManifest", route(publishManifest));
app.post("/verifyPolicy", route(verifyPolicy));
app.post("/verifyConversion", route(verifyConversion));
app.post("/auditBatch", route(auditBatch));

app.listen(3000, "0.0.0.0");
