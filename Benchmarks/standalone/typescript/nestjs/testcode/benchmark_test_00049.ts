// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, UsePipes, ValidationPipe, ForbiddenException } from "@nestjs/common";
import { Response } from "express";
import * as childProcess from "child_process";
import { IsString } from "class-validator";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

class UserInputDto {
  @IsString()
  payload!: string;
}
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
  @Post("BenchmarkTest00049")
  @UsePipes(new ValidationPipe())
  async BenchmarkTest00049(@Body() dto: UserInputDto): Promise<unknown> {
    const userInput = dto.payload;
    let data;
    try { data = JSON.parse(userInput).value || ""; }
    catch (e) { data = String(userInput); }
    if (!["ls", "cat", "date", "whoami"].includes(data)) { throw new ForbiddenException({error:'forbidden'}); }
    const allowedBin = data;
    childProcess.exec("echo " + allowedBin, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
