// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("macro-service")
export class ApplyMacro {
  @Post("applyMacro")
  async applyMacro(@Req() req: Request): Promise<unknown> {
    const subtitle = req.body.support_payload || "";
    http.get(subtitle);
    return { created: true };
  }
}
