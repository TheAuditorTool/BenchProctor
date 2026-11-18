const express = require("express");
const session = require("express-session");

const quoteShipment = require("./shipment_quote").quoteShipment;
const auditWindow = require("./audit_window").auditWindow;
const collectSummary = require("./collect_summary").collectSummary;
const reconcileProfile = require("./reconcile_profile").reconcileProfile;
const exportProfile = require("./export_profile").exportProfile;
const mergeLabel = require("./merge_label").mergeLabel;
const verifyManifest = require("./verify_manifest").verifyManifest;
const verifyWindow = require("./verify_window").verifyWindow;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/quoteShipment", route(quoteShipment));
app.post("/auditWindow", route(auditWindow));
app.post("/collectSummary", route(collectSummary));
app.post("/reconcileProfile", route(reconcileProfile));
app.post("/exportProfile", route(exportProfile));
app.post("/mergeLabel", route(mergeLabel));
app.post("/verifyManifest", route(verifyManifest));
app.post("/verifyWindow", route(verifyWindow));

app.listen(3000, "0.0.0.0");
