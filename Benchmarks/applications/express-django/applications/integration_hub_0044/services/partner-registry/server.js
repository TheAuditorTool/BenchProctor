const express = require("express");
const session = require("express-session");

const registerPartner = require("./partner_register").registerPartner;
const exportDigest = require("./export_digest").exportDigest;
const reconcileSnapshot = require("./reconcile_snapshot").reconcileSnapshot;
const renderSnapshot = require("./render_snapshot").renderSnapshot;
const annotateDigest = require("./annotate_digest").annotateDigest;
const enrichThreshold = require("./enrich_threshold").enrichThreshold;
const resolveWindow = require("./resolve_window").resolveWindow;
const verifyThreshold = require("./verify_threshold").verifyThreshold;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/registerPartner", route(registerPartner));
app.post("/exportDigest", route(exportDigest));
app.post("/reconcileSnapshot", route(reconcileSnapshot));
app.post("/renderSnapshot", route(renderSnapshot));
app.post("/annotateDigest/:id", route(annotateDigest));
app.post("/enrichThreshold", route(enrichThreshold));
app.post("/resolveWindow", route(resolveWindow));
app.post("/verifyThreshold", route(verifyThreshold));

app.listen(3000, "0.0.0.0");
