// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("statement-export")
export class ReconcileWindow {
  @Post("reconcileWindow")
  async reconcileWindow(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers.host as string) || "";
    const remittance = `${headline}`;
    http.get(remittance);
    return { created: true };
  }
}
