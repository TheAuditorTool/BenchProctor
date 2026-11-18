import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { appendAudit } from "./audit_append";
import { exportRoster } from "./export_roster";
import { compactHeader } from "./compact_header";
import { compactQuota } from "./compact_quota";
import { renderPolicy } from "./render_policy";
import { validateTenant } from "./validate_tenant";
import { exportManifest } from "./export_manifest";
import { annotateReport } from "./annotate_report";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/appendAudit", route(appendAudit));
app.post("/exportRoster", route(exportRoster));
app.post("/compactHeader", route(compactHeader));
app.post("/compactQuota", route(compactQuota));
app.post("/renderPolicy", route(renderPolicy));
app.post("/validateTenant", route(validateTenant));
app.post("/exportManifest", route(exportManifest));
app.post("/annotateReport", route(annotateReport));

app.listen(3000, "0.0.0.0");
