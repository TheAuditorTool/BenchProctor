// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("canary-controller")
export class PromoteCanary {
  @Post("promoteCanary")
  async promoteCanary(@Req() req: Request): Promise<unknown> {
    const subject = req.body.delivery_payload || "";
    http.get(subject);
    return { created: true };
  }
}
