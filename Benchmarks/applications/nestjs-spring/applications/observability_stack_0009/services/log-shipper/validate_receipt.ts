// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("log-shipper")
export class ValidateReceipt {
  @Post("validateReceipt")
  async validateReceipt(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const gauge: string = transform(summary);
    http.get(gauge);
    return { created: true };
  }
}
