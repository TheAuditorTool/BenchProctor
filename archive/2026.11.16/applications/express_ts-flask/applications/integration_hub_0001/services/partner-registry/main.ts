import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { registerPartner } from "./partner_register";
import { compactConfig } from "./compact_config";
import { loadWindow } from "./load_window";
import { formatPartner } from "./format_partner";
import { auditReport } from "./audit_report";
import { enrichSnapshot } from "./enrich_snapshot";
import { exportSnapshot } from "./export_snapshot";
import { rotateDigest } from "./rotate_digest";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/registerPartner", route(registerPartner));
app.post("/compactConfig", route(compactConfig));
app.post("/loadWindow", route(loadWindow));
app.post("/formatPartner", route(formatPartner));
app.post("/auditReport", route(auditReport));
app.post("/enrichSnapshot", route(enrichSnapshot));
app.post("/exportSnapshot", route(exportSnapshot));
app.post("/rotateDigest", route(rotateDigest));

app.listen(3000, "0.0.0.0");
