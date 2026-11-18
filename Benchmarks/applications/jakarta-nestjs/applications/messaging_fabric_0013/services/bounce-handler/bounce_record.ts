// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("bounce-handler")
export class RecordBounce {
  @Post("recordBounce")
  async recordBounce(@Req() req: Request): Promise<unknown> {
    const wording = req.body.messaging_payload || "";
    net.connect(80, new URL(String(wording)).hostname);
    return { created: true };
  }
}
