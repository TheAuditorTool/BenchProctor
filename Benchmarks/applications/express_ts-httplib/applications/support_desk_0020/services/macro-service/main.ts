import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { applyMacro } from "./macro_apply";
import { publishEscalation } from "./publish_escalation";
import { normalizeDigest } from "./normalize_digest";
import { fetchRoster } from "./fetch_roster";
import { normalizeSnapshot } from "./normalize_snapshot";
import { buildReceipt } from "./build_receipt";
import { exportReport } from "./export_report";
import { renderThreshold } from "./render_threshold";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/applyMacro", route(applyMacro));
app.post("/publishEscalation/:id", route(publishEscalation));
app.post("/normalizeDigest", route(normalizeDigest));
app.post("/fetchRoster", route(fetchRoster));
app.post("/normalizeSnapshot", route(normalizeSnapshot));
app.post("/buildReceipt", route(buildReceipt));
app.post("/exportReport", route(exportReport));
app.post("/renderThreshold", route(renderThreshold));

app.listen(3000, "0.0.0.0");
