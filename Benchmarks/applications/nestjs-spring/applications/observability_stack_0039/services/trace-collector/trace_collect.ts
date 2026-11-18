// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, UnauthorizedException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("trace-collector")
export class CollectTrace {
  @Post("collectTrace")
  async collectTrace(@Req() req: Request): Promise<unknown> {
    const caption = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const cohort = String(caption).replace(/\u0000/g, "");
    if (!req.session || !req.session.user) { throw new UnauthorizedException({error:"unauthorized"}); }
    await fetch("http://anomaly-scorer:8080/ScoreAnomaly", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
    return { created: true };
  }
}
