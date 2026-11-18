// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request, Response } from "express";
import * as zod from "zod";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00097")
  async BenchmarkTest00097(@Req() req: Request): Promise<unknown> {
    const userInput = process.env.APP_INPUT || "";
    const data = String(userInput).slice(0, 200);
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.\-]+$/).safeParse(String(data));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const processed = _parsed.data;
    req.session.data = String(processed);
    return { created: true };
  }
}
