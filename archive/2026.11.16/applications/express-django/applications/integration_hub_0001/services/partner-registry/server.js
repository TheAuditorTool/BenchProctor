const express = require("express");
const session = require("express-session");

const registerPartner = require("./partner_register").registerPartner;
const compactConfig = require("./compact_config").compactConfig;
const loadWindow = require("./load_window").loadWindow;
const rotateReceipt = require("./rotate_receipt").rotateReceipt;
const fetchConfig = require("./fetch_config").fetchConfig;
const resolveSummary = require("./resolve_summary").resolveSummary;
const exportSummary = require("./export_summary").exportSummary;
const publishSnapshot = require("./publish_snapshot").publishSnapshot;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/registerPartner", route(registerPartner));
app.post("/compactConfig", route(compactConfig));
app.post("/loadWindow", route(loadWindow));
app.post("/rotateReceipt", route(rotateReceipt));
app.post("/fetchConfig", route(fetchConfig));
app.post("/resolveSummary", route(resolveSummary));
app.post("/exportSummary", route(exportSummary));
app.post("/publishSnapshot", route(publishSnapshot));

app.listen(3000, "0.0.0.0");
