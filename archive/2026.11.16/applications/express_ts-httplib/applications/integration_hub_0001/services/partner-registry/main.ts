import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { registerPartner } from "./partner_register";
import { compactConfig } from "./compact_config";
import { loadWindow } from "./load_window";
import { rotateReceipt } from "./rotate_receipt";
import { fetchConfig } from "./fetch_config";
import { resolveSummary } from "./resolve_summary";
import { exportSummary } from "./export_summary";
import { publishSnapshot } from "./publish_snapshot";

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
app.post("/rotateReceipt", route(rotateReceipt));
app.post("/fetchConfig", route(fetchConfig));
app.post("/resolveSummary", route(resolveSummary));
app.post("/exportSummary", route(exportSummary));
app.post("/publishSnapshot", route(publishSnapshot));

app.listen(3000, "0.0.0.0");
