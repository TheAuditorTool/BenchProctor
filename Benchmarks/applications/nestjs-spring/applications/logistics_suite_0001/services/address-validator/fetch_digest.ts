// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("address-validator")
export class FetchDigest {
  @Post("fetchDigest")
  async fetchDigest(@Req() req: Request): Promise<unknown> {
    const quotation = (req.body?.variables?.input as string) || "";
    const parts: string[] = [];
    for (const token of String(quotation).split(',')) { parts.push(token); }
    const parcel: string = parts.join(',');
    const reportSpec = jsYaml.load(String(parcel), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
