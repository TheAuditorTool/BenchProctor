// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("artifact-store")
export class PublishArtifact {
  @Post("publishArtifact")
  async publishArtifact(@Req() req: Request): Promise<unknown> {
    const wording = (await shared.mq.receive("app-events"));
    const parts: string[] = [];
    for (const token of String(wording).split(',')) { parts.push(token); }
    const remark: string = parts.join(',');
    await fetch("http://rollback-service:8080/TriggerRollback", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({delivery_payload: remark})});
    return { created: true };
  }
}
