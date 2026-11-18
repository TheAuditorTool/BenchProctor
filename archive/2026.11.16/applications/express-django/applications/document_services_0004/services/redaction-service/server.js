const express = require("express");
const session = require("express-session");

const applyRedaction = require("./redaction_apply").applyRedaction;
const publishRoster = require("./publish_roster").publishRoster;
const publishLedger = require("./publish_ledger").publishLedger;
const enrichSnapshot = require("./enrich_snapshot").enrichSnapshot;
const annotateProfile = require("./annotate_profile").annotateProfile;
const publishSignature = require("./publish_signature").publishSignature;
const reconcileAttachment = require("./reconcile_attachment").reconcileAttachment;
const summarizeCheckpoint = require("./summarize_checkpoint").summarizeCheckpoint;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/applyRedaction", route(applyRedaction));
app.post("/publishRoster", route(publishRoster));
app.post("/publishLedger", route(publishLedger));
app.post("/enrichSnapshot", route(enrichSnapshot));
app.post("/annotateProfile", route(annotateProfile));
app.post("/publishSignature", route(publishSignature));
app.post("/reconcileAttachment", route(reconcileAttachment));
app.post("/summarizeCheckpoint", route(summarizeCheckpoint));

app.listen(3000, "0.0.0.0");
