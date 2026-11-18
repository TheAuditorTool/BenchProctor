// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("anomaly-scorer")
export class RenderSchedule {
  @Post("renderSchedule")
  async renderSchedule(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers.origin as string) || "";
    const pending: string[] = String(caption).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const cohort: string = collected.join(',');
    nodeSerialize.unserialize(cohort);
    return { created: true };
  }
}
