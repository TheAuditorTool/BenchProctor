const express = require("express");
const session = require("express-session");

const verifySignature = require("./signature_verify").verifySignature;
const reconcileWebhook = require("./reconcile_webhook").reconcileWebhook;
const validateProfile = require("./validate_profile").validateProfile;
const enrichThreshold = require("./enrich_threshold").enrichThreshold;
const exportRoster = require("./export_roster").exportRoster;
const loadBundle = require("./load_bundle").loadBundle;
const mergeConfig = require("./merge_config").mergeConfig;
const auditBundle = require("./audit_bundle").auditBundle;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/verifySignature", route(verifySignature));
app.post("/reconcileWebhook", route(reconcileWebhook));
app.post("/validateProfile", route(validateProfile));
app.post("/enrichThreshold", route(enrichThreshold));
app.post("/exportRoster", route(exportRoster));
app.post("/loadBundle", route(loadBundle));
app.post("/mergeConfig", route(mergeConfig));
app.post("/auditBundle", route(auditBundle));

app.listen(3000, "0.0.0.0");
