import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { composeTemplate } from "./template_compose";
import { verifySubscription } from "./verify_subscription";
import { pruneSubscription } from "./prune_subscription";
import { reconcileIndex } from "./reconcile_index";
import { fetchRecord } from "./fetch_record";
import { resolveIndex } from "./resolve_index";
import { verifyProfile } from "./verify_profile";
import { verifySummary } from "./verify_summary";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/composeTemplate", route(composeTemplate));
app.post("/verifySubscription", route(verifySubscription));
app.post("/pruneSubscription", route(pruneSubscription));
app.post("/reconcileIndex", route(reconcileIndex));
app.post("/fetchRecord", route(fetchRecord));
app.post("/resolveIndex", route(resolveIndex));
app.post("/verifyProfile", route(verifyProfile));
app.post("/verifySummary", route(verifySummary));

app.listen(3000, "0.0.0.0");
