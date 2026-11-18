// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("screening-service")
export class ValidateReceipt {
  @Post("validateReceipt")
  async validateReceipt(@Req() req: Request): Promise<unknown> {
    const subject = (req.headers["user-agent"] as string) || "";
    http.get(subject);
    return { created: true };
  }
}
