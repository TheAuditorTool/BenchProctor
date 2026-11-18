// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("presence-hub")
export class TrackPresence {
  @Post("trackPresence")
  async trackPresence(@Req() req: Request): Promise<unknown> {
    const preface = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const [remark] = String(preface).split(',');
    await fetch("http://share-service:8080/GrantShare", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: remark})});
    return { created: true };
  }
}
