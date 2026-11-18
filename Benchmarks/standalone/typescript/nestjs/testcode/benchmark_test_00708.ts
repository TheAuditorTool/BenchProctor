// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post, BadRequestException } from "@nestjs/common";
import { Response } from "express";
import * as childProcess from "child_process";
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
  @Post("BenchmarkTest00708")
  async BenchmarkTest00708(@Headers("authorization") auth: string): Promise<unknown> {
    const userInput = auth || "";
    const data = userInput != null ? userInput : '';
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(data));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const processed = _parsed.data;
    childProcess.execSync("echo " + processed);
    return { created: true };
  }
}
