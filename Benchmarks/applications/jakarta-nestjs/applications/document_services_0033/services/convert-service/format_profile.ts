// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("convert-service")
export class FormatProfile {
  @Post("formatProfile")
  async formatProfile(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers.origin as string) || "";
    const _raw = snippet;
    const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
    const reportSpec = jsYaml.load(String(addendum), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
