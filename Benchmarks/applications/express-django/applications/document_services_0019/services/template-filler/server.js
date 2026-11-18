const express = require("express");
const session = require("express-session");

const fillTemplate = require("./template_fill").fillTemplate;
const verifyRoster = require("./verify_roster").verifyRoster;
const auditRecord = require("./audit_record").auditRecord;
const compactLedger = require("./compact_ledger").compactLedger;
const verifyBundle = require("./verify_bundle").verifyBundle;
const resolveProfile = require("./resolve_profile").resolveProfile;
const archiveBatch = require("./archive_batch").archiveBatch;
const annotateConfig = require("./annotate_config").annotateConfig;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/fillTemplate", route(fillTemplate));
app.post("/verifyRoster", route(verifyRoster));
app.post("/auditRecord", route(auditRecord));
app.post("/compactLedger", route(compactLedger));
app.post("/verifyBundle", route(verifyBundle));
app.post("/resolveProfile", route(resolveProfile));
app.post("/archiveBatch", route(archiveBatch));
app.post("/annotateConfig", route(annotateConfig));

app.listen(3000, "0.0.0.0");
