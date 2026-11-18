// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("attachment-store")
export class StoreAttachment {
  @Post("storeAttachment")
  async storeAttachment(@Req() req: Request): Promise<unknown> {
    const remark = (await shared.mq.receive("app-events"));
    const pending: string[] = String(remark).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const inquiry: string = collected.join(',');
    await fetch("http://survey-service:8080/SendSurvey", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
    return { created: true };
  }
}
