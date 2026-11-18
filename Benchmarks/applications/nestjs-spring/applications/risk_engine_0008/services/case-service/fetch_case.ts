// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("case-service")
export class FetchCase {
  @Post("fetchCase")
  async fetchCase(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const verdict: string = transform(synopsis);
    http.get(verdict);
    return { created: true };
  }
}
