import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { configureSample } from "./sample_config";
import { collectSnapshot } from "./collect_snapshot";
import { resolveSummary } from "./resolve_summary";
import { fetchWindow } from "./fetch_window";
import { fetchConfig } from "./fetch_config";
import { compactPolicy } from "./compact_policy";
import { summarizeSnapshot } from "./summarize_snapshot";
import { archiveSummary } from "./archive_summary";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/configureSample", route(configureSample));
app.post("/collectSnapshot", route(collectSnapshot));
app.post("/resolveSummary", route(resolveSummary));
app.post("/fetchWindow", route(fetchWindow));
app.post("/fetchConfig", route(fetchConfig));
app.post("/compactPolicy", route(compactPolicy));
app.post("/summarizeSnapshot", route(summarizeSnapshot));
app.post("/archiveSummary", route(archiveSummary));

app.listen(3000, "0.0.0.0");
