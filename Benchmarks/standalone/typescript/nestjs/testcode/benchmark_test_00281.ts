// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post, BadRequestException } from "@nestjs/common";
import { Response } from "express";
import * as childProcess from "child_process";
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
  @Post("BenchmarkTest00281")
  async BenchmarkTest00281(@Headers("authorization") auth: string): Promise<unknown> {
    const userInput = auth || "";
    const [data] = String(userInput).split(',');
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(data)) { throw new BadRequestException({error:"invalid"}); }
    const processed = data;
    childProcess.spawn("echo " + processed, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}
