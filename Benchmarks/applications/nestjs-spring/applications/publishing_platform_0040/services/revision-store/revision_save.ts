// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("revision-store")
export class SaveRevision {
  @Post("saveRevision")
  async saveRevision(@Req() req: Request): Promise<unknown> {
    const transcript = (req.query.id as string) || "";
    const addendum = Buffer.from(transcript, "hex").toString();
    await fetch("http://syndication-feed:8080/PushSyndication", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: addendum})});
    return { created: true };
  }
}
