// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("presence-hub")
export class RotateDocument {
  @Post("rotateDocument")
  async rotateDocument(@Req() req: Request): Promise<unknown> {
    const remark = (await shared.mq.receive("app-events"));
    const pending: string[] = String(remark).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const synopsis: string = collected.join(',');
    JSON.parse(synopsis);
    return { created: true };
  }
}
