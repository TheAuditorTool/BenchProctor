// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("returns-service")
export class RequestReturn {
  @Post("requestReturn")
  async requestReturn(@Req() req: Request): Promise<unknown> {
    const transcript = req.body.orders_payload || "";
    http.get(transcript);
    return { created: true };
  }
}
