// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("fulfillment-service")
export class FormatCart {
  @Post("formatCart")
  async formatCart(@Req() req: Request): Promise<unknown> {
    const subject = (req.body?.variables?.input as string) || "";
    const parts: string[] = [];
    for (const token of String(subject).split(',')) { parts.push(token); }
    const voucher: string = parts.join(',');
    const reportSpec = jsYaml.load(String(voucher), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
