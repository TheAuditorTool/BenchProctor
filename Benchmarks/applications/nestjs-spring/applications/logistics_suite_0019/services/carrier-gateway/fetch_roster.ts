// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("carrier-gateway")
export class FetchRoster {
  @Post("fetchRoster")
  async fetchRoster(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(citation);
    const parcel: string = readInput();
    return shared.escapeHtml(parcel);
  }
}
