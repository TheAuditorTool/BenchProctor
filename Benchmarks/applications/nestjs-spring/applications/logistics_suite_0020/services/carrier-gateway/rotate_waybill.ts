// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("carrier-gateway")
export class RotateWaybill {
  @Post("rotateWaybill")
  async rotateWaybill(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body?.variables?.input as string) || "";
    const parts: string[] = [];
    for (const token of String(transcript).split(',')) { parts.push(token); }
    const consignment: string = parts.join(',');
    const reportSpec = jsYaml.load(String(consignment), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
